import math
import numpy as np



class IRC6_2017:
    def cl_203_dead_load():
        # Clause 203 Dead Load
        """Returns dead load values for various materials in t/m3 as per IRC:6-2017 Clause 203."""
        dead_load = {}
        dead_load['ashlar_granite'] = 2.7  # t/m3
        dead_load['ashlar_sandstone'] = 2.4  # t/m3
        dead_load['stone_setts_granite'] = 2.6  # t/m3
        dead_load['stone_setts_basalt'] = 2.7  # t/m3
        dead_load['ballast_granite'] = 1.4  # t/m3
        dead_load['ballast_basalt'] = 1.6  # t/m3
        dead_load['brickwork_pressed_cement'] = 2.2  # t/m3
        dead_load['brickwork_common_cement'] = 1.9  # t/m3
        dead_load['brickwork_common_lime'] = 1.8  # t/m3
        dead_load['concrete_asphalt'] = 2.2  # t/m3
        dead_load['concrete_bitumen'] = 1.4  # t/m3
        dead_load['concrete_cement_plain'] = 2.5  # t/m3
        dead_load['concrete_cement_plain_plums'] = 2.5  # t/m3
        dead_load['concrete_cement_reinforced'] = 2.5  # t/m3
        dead_load['concrete_cement_prestressed'] = 2.5  # t/m3
        dead_load['concrete_lime_brick'] = 1.9  # t/m3
        dead_load['concrete_lime_stone'] = 2.1  # t/m3
        dead_load['earth_compacted'] = 2.0  # t/m3
        dead_load['gravel'] = 1.8  # t/m3
        dead_load['macadam_binder'] = 2.2  # t/m3
        dead_load['macadam_rolled'] = 2.6  # t/m3
        dead_load['sand_loose'] = 1.7  # t/m3
        dead_load['sand_wet'] = 1.9  # t/m3
        dead_load['rubble_stone_coursed'] = 2.6  # t/m3
        dead_load['stone_masonry_lime'] = 2.4  # t/m3
        dead_load['water'] = 1.0  # t/m3
        dead_load['wood'] = 0.8  # t/m3
        dead_load['cast_iron'] = 7.2  # t/m3
        dead_load['wrought_iron'] = 7.7  # t/m3
        dead_load['steel'] = 7.8  # t/m3
        return dead_load
    
    def cl_204_1_70R_vehicle():
        # Clause 204.1.1 - 70R Vehicle Load
        """Returns the axle load configuration for a 70R vehicle as per IRC:6-2017 Clause 204.1.1."""
        # Axle loads in kN (converted from user input)
        wheel_load = [80.0, 120.0, 120.0, 170.0, 170.0, 170.0, 170.0]

        # Longitudinal axle positions (user-provided)
        load_positions_x = [0.0, 3.96, 5.48, 7.61, 8.98, 12.03, 13.4]

        # Transverse wheel coordinates (user-provided)
        load_positions_z = [-1.19, -0.75, 1.19, 0.75]

        # Create compound load container
        vehicle_load = og.create_compound_load(name="New_70R")

        # Generate load pattern
        for z_pos in load_positions_z:
            for axle_idx, x_pos in enumerate(load_positions_x):

                # Create load vertex
                load_vert = og.create_load_vertex(
                    x=x_pos,
                    z=z_pos,
                    p=wheel_load[axle_idx]
                )

                # Create point load
                point_load = og.create_load(
                    loadtype="point",
                    name=f"New_70R_Axle{axle_idx+1}_Pos{z_pos}m",
                    point1=load_vert
                )

                # Add to compound load
                vehicle_load.add(point_load)

        return vehicle_load
    
    def cl_204_1_class_A_vehicle():
        # Clause 204.1.1 - 70R Vehicle Load
        """Returns the axle load configuration for a 70R vehicle as per IRC:6-2017 Clause 204.1.1."""
        # Axle loads in kN (converted from user input)
        wheel_load = [80.0, 120.0, 120.0, 170.0, 170.0, 170.0, 170.0]

        # Longitudinal axle positions (user-provided)
        load_positions_x = [0.0, 3.96, 5.48, 7.61, 8.98, 12.03, 13.4]

        # Transverse wheel coordinates (user-provided)
        load_positions_z = [-1.19, -0.75, 1.19, 0.75]

        # Create compound load container
        vehicle_load = og.create_compound_load(name="New_Class_A")

        # Generate load pattern
        for z_pos in load_positions_z:
            for axle_idx, x_pos in enumerate(load_positions_x):

                # Create load vertex
                load_vert = og.create_load_vertex(
                    x=x_pos,
                    z=z_pos,
                    p=wheel_load[axle_idx]
                )

                # Create point load
                point_load = og.create_load(
                    loadtype="point",
                    name=f"New_Class_A_Axle{axle_idx+1}_Pos{z_pos}m",
                    point1=load_vert
                )

                # Add to compound load
                vehicle_load.add(point_load)

        return vehicle_load

    
