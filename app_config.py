import yaml

with open("app_config.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


class AppConfig:
    def get(key):
        child = cfg
        for k in key.split("."):
            child = child.get(k)

            if not child:
                break

        return child


# AppConfig.get("other.preprocessing_queue")
