from src.model.explorer import Explorer
import src.testdata.explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()


def get_by_name(name: str) -> Explorer | None:
    return data.get_by_name(name)


def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def replace(id, explorer: Explorer) -> Explorer:
    return data.replace(id, explorer)


def modify(id, explorer: Explorer) -> Explorer:
    return data.modify(id, explorer)
