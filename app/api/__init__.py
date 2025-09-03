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
    api_package = importlib.util.find_spec(__name__)
    if not api_package or not api_package.submodule_search_locations:
        return

    # 迭代 app.api 目錄下的所有模組
    # importer：一個載入器（loader）物件，負責載入模組。你通常不需要直接使用它，但它提供了像 find_spec() 這樣的函式。
    # modname : 模組或子套件的名稱。在你的專案中，它可能是 'auth' 或 'user'
    # ispkg : true : 是一個子套件 (有 __init__.py)，false : 是一個模組 (.py)
    for importer, modname, ispkg in pkgutil.walk_packages(api_package.__path__):
        if ispkg:
            continue

        module = importer.find_module(modname).load_module(modname)

        # 遍歷模組中的所有屬性
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            # 檢查屬性是否為 APIRouter 的實例
            if isinstance(attr, APIRouter):
                print(f"自動載入路由: {modname}.{attr_name}")
                router.include_router(attr)


# 在這個套件載入時，自動執行註冊
register_routers()


