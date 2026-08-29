import os
from logger import export_logs_to_file

def test_export_logs_to_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file_path = d / "test_log.txt"
    logs = ["error 1", "error 2"]
    export_logs_to_file(str(file_path), logs)
    assert file_path.read_text() == "error 1\nerror 2\n"