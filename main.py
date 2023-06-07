import pathlib

from trainer.application import Trainer

if __name__ == "__main__":
    app = Trainer(pathlib.Path("UTPackages/Example").resolve())
    app.run()
