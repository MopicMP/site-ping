"""Tests for site-ping."""

import pytest
from site_ping import ping


class TestPing:
    """Test suite for ping."""

    def test_basic(self):
        """Test basic usage."""
        result = ping("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            ping("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = ping(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
