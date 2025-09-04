import importlib.util
import pkgutil

from fastapi import APIRouter

router = APIRouter()

def register_routers():
    """自動註冊 app/api/ 目錄下的所有 APIRouter"""
    # 獲取 app.api 目錄的 package 資訊
    # 模組 (Module)：通常是一個單一的 .py 檔案。它沒有 submodule_search_locations 這個屬性。
    # 套件 (Package)：一個包含 __init__.py 檔案的目錄，可以包含多個子模組或子套件。
    # 它有 submodule_search_locations 這個屬性
    # 獲取當前套件 (app.api) 的路徑。
    # __path__ 是一個列表，包含了套件所有子模組的路徑，這是 pkgutil.walk_packages 所需要的。
    # 如果這個檔案是 __init__.py，則 __name__ 代表套件名稱，而 __path__ 則代表套件路徑。
    # 使用 `globals()` 獲取當前模組的 __path__ 屬性
    package_path = globals()['__path__']

    # 使用 pkgutil.walk_packages 迭代 app.api 目錄下的所有模組
    # importer: 模組的載入器物件
    # modname: 模組或子套件的名稱
    # ispkg: true : 是一個子套件 (有 __init__.py)，false : 是一個模組 (.py)
    for importer, modname, ispkg in pkgutil.walk_packages(package_path):
        # 忽略子套件，只處理 .py 模組
        if ispkg:
            continue

        # 使用 importlib.import_module 載入模組，這是更現代的方式
        # 這裡需要完整的模組路徑，例如 'app.api.users'
        full_module_name = f"{__name__}.{modname}"
        try:
            module = importlib.import_module(full_module_name)
        except ImportError as e:
            print(f"無法載入模組 {full_module_name}: {e}")
            continue

        # 遍歷模組中的所有屬性
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            # 檢查屬性是否為 APIRouter 的實例
            if isinstance(attr, APIRouter):
                print(f"自動載入路由: {modname}.{attr_name}")
                router.include_router(attr)


# 在這個套件載入時，自動執行註冊
register_routers()


