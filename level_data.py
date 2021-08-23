class Level:
    """
    """
    def __init__(self):
        """
        """
        #walls
        #intersections
        #call level building methods

    def intersections_spawn(self):
        """
        """
        # Place Intersections (for ghost movement)
        for isect in intersections:
            intersection = Intersection(6, isect[2])
            intersection.rect.x = 30 * isect[0] + 32
            intersection.rect.y = 30 * isect[1] + 32
            intersection_group.add(intersection)
            all_sprites_group.add(intersection)

    def setup_room1(self):
        pass

    def setup_gate():
        pass

    def dots_spawn(self):
        #block_spawn?
        """
        """
        # Draw the grid
        for row in range(19):
            for column in range(19):

                # Don't spawn blocks/dots behind the gate (ghost spawn area)
                if (row in (7, 8)) and (column in (8, 9, 10)):
                    continue
                else:
                    # Spawn the blocks/dots
                    block = Block(4, 4, yellow)
    
                    # Set the block positions so that they are spaced out
                    block.rect.x = 30 * column + 32
                    block.rect.y = 30 * row + 32
    
                    # Don't spawn a block/dot where the walls or player is
                    b_collide = pygame.sprite.spritecollide(block, wall_group, False)
                    p_collide = pygame.sprite.spritecollide(
                                                        block, pacman_collide, False)
                    if b_collide:
                        continue
                    elif p_collide:
                        continue
                    else:
                        # Add the block to the list of objects
                        block_group.add(block)
                        all_sprites_group.add(block)


# This is a list of walls. Each is in the form [x, y, width, height]
walls = [[0,0,6,600],
         [0,0,600,6],
         [0,600,606,6],
         [600,0,6,606],
         [300,0,6,66],
         [60,60,186,6],
         [360,60,186,6],
         [60,120,66,6],
         [60,120,6,126],
         [180,120,246,6],
         [300,120,6,66],
         [480,120,66,6],
         [540,120,6,126],
         [120,180,126,6],
         [120,180,6,126],
         [360,180,126,6],
         [480,180,6,126],
         [180,240,6,126],
         [180,360,246,6],
         [420,240,6,126],
         [240,240,42,6],
         [324,240,42,6],
         [240,240,6,66],
         [240,300,126,6],
         [360,240,6,66],
         [0,300,66,6],
         [540,300,66,6],
         [60,360,66,6],
         [60,360,6,186],
         [480,360,66,6],
         [540,360,6,186],
         [120,420,366,6],
         [120,420,6,66],
         [480,420,6,66],
         [180,480,246,6],
         [300,480,6,66],
         [120,540,126,6],
         [360,540,126,6]]

intersections = [(0, 2, {'up', 'down', 'right'}),
                 (4, 2, {'down', 'left', 'right'}),
                 (8, 2, {'up', 'left', 'right'}),
                 (10, 2, {'up', 'left', 'right'}),
                 (14, 2, {'down', 'left', 'right'}),
                 (18, 2, {'up', 'down', 'left'}),
                 (4, 4, {'up', 'left', 'right'}),
                 (14, 4, {'up', 'left', 'right'}),
                 (6, 6, {'down', 'left', 'right'}),
                 (8, 6, {'up', 'left', 'right'}),
                 (10, 6, {'up', 'left', 'right'}),
                 (12, 6, {'down', 'left', 'right'}),
                 (2, 8, {'up', 'down', 'left'}),
                 (9, 8, {'up', 'left', 'right'}),
                 (16, 8, {'up', 'down', 'right'}),
                 (2, 10, {'up', 'left', 'right'}),
                 (4, 10, {'up', 'down', 'left'}),
                 (14, 10, {'up', 'down', 'right'}),
                 (16, 10, {'up', 'left', 'right'}),
                 (4, 12, {'up', 'left', 'right'}),
                 (14, 12, {'up', 'left', 'right'}),
                 (2, 16, {'up', 'down', 'right'}),
                 (4, 16, {'up', 'left', 'right'}),
                 (14, 16, {'up', 'left', 'right'}),
                 (16, 16, {'up', 'down', 'left'}),
                 (2, 18, {'up', 'left', 'right'}),
                 (8, 18, {'up', 'left', 'right'}),
                 (10, 18, {'up', 'left', 'right'}),
                 (16, 18, {'up', 'left', 'right'})]