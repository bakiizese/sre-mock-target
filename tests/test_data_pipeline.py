import os
from backend.analytics.data_pipeline import export_logs_to_file

def test_export_logs_to_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file_path = d / "test_log.txt"
    entries = ["log1", "log2", "log3"]
    
    export_logs_to_file(str(file_path), entries)
    
    assert file_path.exists()
    content = file_path.read_text()
    assert "log1\nlog2\nlog3\n" in content
