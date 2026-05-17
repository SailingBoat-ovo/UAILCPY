import sys
import io
import contextlib


def normalize_output(text):
    lines = text.strip().split("\n")
    normalized = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            normalized.append(stripped)
    return "\n".join(normalized)


def check_python(code, sample_input, expected_output):
    try:
        output_io = io.StringIO()
        input_io = io.StringIO(sample_input)

        compiled = compile(code, "<student_code>", "exec")

        global_ns = {"__builtins__": __builtins__}

        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = input_io
        sys.stdout = output_io

        try:
            exec(compiled, global_ns)
        except Exception as e:
            return False, f"\u8fd0\u884c\u9519\u8bef: {type(e).__name__}: {e}"
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

        actual = normalize_output(output_io.getvalue())
        expected = normalize_output(expected_output)

        if actual == expected:
            return True, "\u901a\u8fc7\uff01\u8f93\u51fa\u5b8c\u5168\u6b63\u786e\uff01"
        else:
            diff = _build_diff(actual, expected)
            return False, "\u8f93\u51fa\u4e0d\u5339\u914d:\n\u4f60\u7684\u8f93\u51fa:\n" + actual + "\n\n\u671f\u671b\u8f93\u51fa:\n" + expected + "\n\n\u5dee\u5f02\u5bf9\u6bd4:\n" + "\n".join(diff)

    except SyntaxError as e:
        return False, f"\u8bed\u6cd5\u9519\u8bef: \u7b2c{e.lineno}\u884c: {e.msg}\n{e.text}"
    except Exception as e:
        return False, f"\u9519\u8bef: {type(e).__name__}: {e}"


def check_cpp_output(user_output, expected_output):
    actual = normalize_output(user_output)
    expected = normalize_output(expected_output)

    if actual == expected:
        return True, "\u901a\u8fc7\uff01\u8f93\u51fa\u5b8c\u5168\u6b63\u786e\uff01"
    else:
        diff = _build_diff(actual, expected)
        return False, "\u8f93\u51fa\u4e0d\u5339\u914d:\n\u4f60\u7684\u8f93\u51fa:\n" + actual + "\n\n\u671f\u671b\u8f93\u51fa:\n" + expected + "\n\n\u5dee\u5f02\u5bf9\u6bd4:\n" + "\n".join(diff)


def _build_diff(actual, expected):
    diff_lines = []
    actual_lines = actual.split("\n")
    expected_lines = expected.split("\n")
    max_len = max(len(actual_lines), len(expected_lines))
    for i in range(max_len):
        a = actual_lines[i] if i < len(actual_lines) else "(\u7f3a\u5c11)"
        e = expected_lines[i] if i < len(expected_lines) else "(\u7f3a\u5c11)"
        if a != e:
            diff_lines.append(f"  \u7b2c{i+1}\u884c: \u671f\u671b '{e}' \uff0c\u4f60\u7684 '{a}'")
        else:
            diff_lines.append(f"  \u7b2c{i+1}\u884c: \u6b63\u786e '{a}'")
    return diff_lines
