import os
from logger import export_logs_to_file

def test_export_logs_to_file_closes_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    filepath = d / "logs.txt"
    logs = ["log1", "log2"]
    
    export_logs_to_file(str(filepath), logs)
    
    # Ensure file exists and contains expected data
    assert filepath.read_text() == "log1\nlog2\n"
    
    # Verify file can be deleted/manipulated immediately, confirming the descriptor is closed
    try:
        os.remove(str(filepath))
    except PermissionError:
        assert False, "File descriptor was leaked and not properly closed."