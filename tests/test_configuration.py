from app.configuration import load_config, AppConfig


def test_default_configuration_paths():
    config: AppConfig = load_config()
    assert config.paths.data_dir.name == "data"
    assert config.paths.artifacts_dir.name == "artifacts"
    assert config.paths.logs_dir.name == "logs"
    assert config.paths.outputs.runs_dir.name == "runs"
    assert config.paths.outputs.checkpoints_dir.name == "checkpoints"
