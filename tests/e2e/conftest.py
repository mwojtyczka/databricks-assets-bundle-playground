import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture
def debug_env_name():
    return "ws2"  # defined in ~/.databricks/debug-env.json
