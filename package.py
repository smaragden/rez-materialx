name = "materialx"

version = "1.35.4"

description = \
    """
    MaterialX
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "os-**", "python-*.*"]
    return [expand_requires(*requires)]

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
    if building:
    	env.CMAKE_MODULE_PATH.append("{root}/cmake")
