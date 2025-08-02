from shapely.geometry import Point

def filter_by_radius(gdf, longitude, latitude, radius_km):
    pt = Point(longitude, latitude)
    buffer = pt.buffer(radius_km / 111)  # rough approximation: 1 deg ~= 111 km
    return gdf[gdf.geometry.intersects(buffer)]
