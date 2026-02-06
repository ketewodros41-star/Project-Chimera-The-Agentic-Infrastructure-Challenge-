import pytest
import importlib

def test_skill_download_interface():
    """
    Validates that the Download Skill interface exists at the spec-defined boundary.
    Asserts compliance with Skill README contracts.
    """
    # Boundary Discovery (No direct import of internals)
    try:
        module = importlib.import_module("chimera.skills")
        skill_download_content = getattr(module, "skill_download_content")
    except (ImportError, AttributeError):
        pytest.fail("Download Skill interface NOT found at chimera.skills")

    # TDD: Must FAIL until implemented (Empty Slot)
    with pytest.raises(NotImplementedError) as excinfo:
        skill_download_content(url="https://youtube.com/test", provider="youtube")
    
    assert "pending agentic implementation" in str(excinfo.value)
