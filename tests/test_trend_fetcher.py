import pytest

def test_trend_data_structure():
    """
    Asserts that the trend data structure matches the API contract in specs/technical.md
    """
    # This import will fail since the module doesn't exist yet
    from chimera.fetcher import fetch_latest_trends
    
    trends = fetch_latest_trends()
    
    assert isinstance(trends, list)
    if len(trends) > 0:
        trend = trends[0]
        assert "trend_id" in trend
        assert "source" in trend
        assert "topic" in trend
        assert "velocity" in trend
        assert isinstance(trend["velocity"], float)
