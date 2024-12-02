import json
from pathlib import Path

from app.exceptions import ConfigError
from . import BASE_DIR
from dataclasses import dataclass


@dataclass
class OutputPaths:
    runs_dir: Path
    checkpoints_dir: Path


@dataclass
class AppPaths:
    data_dir: Path
    artifacts_dir: Path
    logs_dir: Path
    outputs: OutputPaths


@dataclass
class AppConfig:
    paths: AppPaths


def load_config(config_path: Path = BASE_DIR / "config.json") -> AppConfig:
    with config_path.open() as f:
        data = json.load(f)
        if "paths" not in data:
            raise ConfigError("Missing required 'paths' section")
        paths_section = data["paths"]

        if "data_dir" not in paths_section:
            raise ConfigError("Missing required 'data_dir' path")
        data_dir = Path(paths_section["data_dir"])
        if "artifacts_dir" not in paths_section:
            raise ConfigError("Missing required 'artifacts_dir' path")
        artifacts_dir = Path(paths_section["artifacts_dir"])
        if "logs_dir" not in paths_section:
            raise ConfigError("Missing required 'logs_dir' path")
        logs_dir = Path(paths_section["logs_dir"])

        if "outputs" not in paths_section:
            raise ConfigError("Missing required 'outputs' path section")
        outputs_path_section = paths_section["outputs"]

        if "runs_dir" not in outputs_path_section:
            raise ConfigError("Missing required 'runs_dir' output")
        runs_dir = Path(outputs_path_section["runs_dir"])
        if "checkpoints_dir" not in outputs_path_section:
            raise ConfigError("Missing required 'checkpoints_dir' output")
        checkpoints_dir = Path(outputs_path_section["checkpoints_dir"])

        return AppConfig(
            paths=AppPaths(
                data_dir=data_dir,
                artifacts_dir=artifacts_dir,
                logs_dir=logs_dir,
                outputs=OutputPaths(
                    runs_dir=runs_dir,
                    checkpoints_dir=checkpoints_dir,
                ),
            )
        )
