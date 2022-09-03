from openeo.udf import XarrayDataCube

def apply_datacube(cube: XarrayDataCube, context: dict) -> XarrayDataCube:
    """
    A trivial UDF that scales values, can also be done without UDF!
    """
    array = cube.get_array()
    array.values = 0.0001 * array.values
    return cube