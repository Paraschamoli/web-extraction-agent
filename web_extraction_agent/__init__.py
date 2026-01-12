# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""web-extraction-agent - A Bindu Agent for web content extraction and structuring."""

from web_extraction_agent.__version__ import __version__
from web_extraction_agent.main import (
    APIKeyError,
    ContentSection,
    PageInformation,
    cleanup,
    handler,
    initialize_agent,
    main,
    run_agent,
)

__all__ = [
    "APIKeyError",
    "ContentSection",
    "PageInformation",
    "__version__",
    "cleanup",
    "handler",
    "initialize_agent",
    "main",
    "run_agent",
]
