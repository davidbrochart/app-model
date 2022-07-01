"""Generic application schema implemented in python."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("app-model")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "uninstalled"

from ._app import Application

__all__ = ["__version__", "Application"]
