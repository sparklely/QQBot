import yaml


class YamlConfiguration:
    def __init__(self, path):
        self.data = {}
        self.path = path

        if path.exists():
            with open(path, "r") as f:
                yaml_data = yaml.safe_load(f)
                if yaml_data:
                    self.data = yaml_data

    def get(self, path):
        keys = path.split(".")
        current = self.data
        for key in keys[:-1]:
            if isinstance(current, dict):
                current = current.get(key)
            else:
                return None
        return current.get(keys[-1])

    def set(self, path, value):
        keys = path.split(".")
        current = self.data
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value

    def save(self):
        with open(self.path, "w") as f:
            yaml.dump(self.data, f)

    def get_string(self, path):
        return self.get(path)

    def get_int(self, path):
        return int(self.get(path))

    def get_boolean(self, path):
        return bool(self.get(path))
