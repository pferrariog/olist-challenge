from dynaconf import Dynaconf


settings = Dynaconf(settings_file="settings.yaml", environments=False)
