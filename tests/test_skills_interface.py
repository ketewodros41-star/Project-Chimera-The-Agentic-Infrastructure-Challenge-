import pytest
import importlib

def test_skill_download_interface_compliance():
    """
    Validates that the Download Skill interface exists.
    Asserts against parameter contracts in skills/README.md. [TR-T2]
    Must FAIL with NotImplementedError on Day 3.
    """
    # Boundary Discovery
    try:
        module = importlib.import_module("chimera.skills")
        skill_download_content = getattr(module, "skill_download_content")
    except (ImportError, AttributeError):
        pytest.fail("Download Skill interface NOT found at chimera.skills")

    # Skill input parameter contracts validation (intent)
    # Input: {"url": "string", "provider": "string"}
    
    # Output type assertions (intent)
    # Expected: dict containing {"local_path": str, "bytes": int}
    
    # TDD: Must FAIL until implemented (Empty Slot)
    skill_download_content(url="https://youtube.com/test", provider="youtube")
