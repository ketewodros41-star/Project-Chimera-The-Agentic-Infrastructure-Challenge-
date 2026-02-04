import pytest

def test_skill_download_interface():
    """
    Asserts that the skill_download_content module accepts correct parameters
    """
    # This import will fail since the module doesn't exist yet
    from chimera.skills import skill_download_content
    
    result = skill_download_content(url="https://youtube.com/test", provider="youtube")
    
    assert "local_path" in result
    assert "bytes" in result
