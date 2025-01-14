Dictionaries for faster lookup.
==============================================

- For faster lookup, the GTFS set is post-processed into several dictionaries and provided as pickle files. 
    - stops_dict_pkl: Contains stops along the route. Format: {route_id: list of stops}
    - stoptimes_dict_pkl: Contains trips along a route. Format: {route_id: [trip_1, trip_2]}
    - transfers_dict_full: Contains footpath details. Format: {stop_id: [(stop_id, time)]}
    - routes_by_stop: All routes passing from a given stop id. Format: {stop_id: list of routes}
    - idx_by_route_stop: Gives the index of a stop along a route. Format: {(route_id, stop_id): index}

  Functions for building these dicts from the GTFS set are present in `dict_builder.py <https://github.com/transnetlab/transit-routing/blob/main/dict_builder/dict_builder_functions.py>`_.

Description
------------------------------------------

.. automodule:: dict_builder.dict_builder_functions
   :members:
