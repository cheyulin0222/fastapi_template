import pkgutil

from fastapi import APIRouter

router = APIRouter()

def register_routers():
    """自動註冊 app/api/ 目錄下的所有 APIRouter"""
    # 獲取 app.api 目錄的 package 資訊
    api_package = pkgutil.get_loader(__name__).load_module(__name__)

    # 迭代 app.api 目錄下的所有模組
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


