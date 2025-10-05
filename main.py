@namespace
class SpriteKind:
    cursor = SpriteKind.create()
    Monster = SpriteKind.create()

def on_overlap_tile(sprite3, location2):
    if controller.B.is_pressed():
        tiles.set_wall_at(location2, False)
        tiles.set_tile_at(location2, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Iron ore
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite14, location13):
    if controller.B.is_pressed():
        tiles.set_wall_at(location13, False)
        tiles.set_tile_at(location13, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Planks
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite13, location12):
    if controller.B.is_pressed():
        tiles.set_wall_at(location12, False)
        tiles.set_tile_at(location12, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Glass
        """),
    on_overlap_tile3)

def on_overlap_tile4(sprite5, location4):
    if controller.B.is_pressed():
        tiles.set_wall_at(location4, False)
        tiles.set_tile_at(location4, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Leaves
        """),
    on_overlap_tile4)

def Def_list():
    global Tile_map_list, Block_list
    Tile_map_list = [tilemap("""
            World 1
            """),
        tilemap("""
            World 2
            """),
        tilemap("""
            World 3
            """),
        tilemap("""
            World 4
            """),
        tilemap("""
            World 5
            """),
        tilemap("""
            World 6
            """),
        tilemap("""
            World 7
            """),
        tilemap("""
            World 8
            """),
        tilemap("""
            World 9
            """),
        tilemap("""
            Superflat
            """)]
    Block_list = [assets.tile("""
            Stone
            """),
        assets.tile("""
            Grass
            """),
        assets.tile("""
            Dirt
            """),
        assets.tile("""
            Log
            """),
        assets.tile("""
            Leaves
            """),
        assets.tile("""
            Log with leaves
            """),
        assets.tile("""
            Planks
            """),
        assets.tile("""
            Diamond ore
            """),
        assets.tile("""
            Glass
            """),
        assets.tile("""
            Iron ore
            """),
        assets.tile("""
            Coal ore
            """),
        assets.tile("""
            Bedrock
            """)]

def on_overlap_tile5(sprite10, location9):
    if controller.B.is_pressed():
        tiles.set_wall_at(location9, False)
        tiles.set_tile_at(location9, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Diamond ore
        """),
    on_overlap_tile5)

def on_on_overlap(sprite2, otherSprite):
    if controller.B.is_pressed():
        music.play(music.create_song(assets.song("""
                Hit
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        sprites.destroy(otherSprite, effects.disintegrate, 500)
        info.change_score_by(1)
        Respawn_slime()
sprites.on_overlap(SpriteKind.cursor, SpriteKind.enemy, on_on_overlap)

def Init_start():
    global Steve, Cursor, Cursor_left, Menu, Block, Block_name, Down, Up, Night, Inventory
    tiles.set_current_tilemap(Tile_map_list._pick_random())
    Steve = sprites.create(assets.image("""
        Steve right
        """), SpriteKind.player)
    scene.camera_follow_sprite(Steve)
    Steve.set_stay_in_screen(True)
    Steve.set_flag(SpriteFlag.GHOST_THROUGH_SPRITES, False)
    Cursor = sprites.create(assets.image("""
        Cursor
        """), SpriteKind.cursor)
    Cursor.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    Cursor_left = False
    Menu = False
    Block = assets.tile("""
        Grass
        """)
    Block_name = "Grass"
    Down = False
    Up = False
    Night = False
    Inventory = miniMenu.create_menu(miniMenu.create_menu_item("Stone", assets.tile("""
            Stone
            """)),
        miniMenu.create_menu_item("Grass", assets.tile("""
            Grass
            """)),
        miniMenu.create_menu_item("Dirt", assets.tile("""
            Dirt
            """)),
        miniMenu.create_menu_item("Log", assets.tile("""
            Log
            """)),
        miniMenu.create_menu_item("Leaves", assets.tile("""
            Leaves
            """)),
        miniMenu.create_menu_item("Log with leaves",
            assets.tile("""
                Log with leaves
                """)),
        miniMenu.create_menu_item("Planks", assets.tile("""
            Planks
            """)),
        miniMenu.create_menu_item("Diamond ore", assets.tile("""
            Diamond ore
            """)),
        miniMenu.create_menu_item("Glass", assets.tile("""
            Glass
            """)),
        miniMenu.create_menu_item("Iron ore", assets.tile("""
            Iron ore
            """)),
        miniMenu.create_menu_item("Coal ore", assets.tile("""
            Coal ore
            """)),
        miniMenu.create_menu_item("Bedrock", assets.tile("""
            Bedrock
            """)))
    Inventory.close()
    music.set_volume(255)

def on_overlap_tile6(sprite11, location10):
    if controller.B.is_pressed():
        tiles.set_wall_at(location10, False)
        tiles.set_tile_at(location10, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Coal ore
        """),
    on_overlap_tile6)

def on_overlap_tile7(sprite12, location11):
    if controller.B.is_pressed():
        tiles.set_wall_at(location11, False)
        tiles.set_tile_at(location11, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Stone
        """),
    on_overlap_tile7)

def on_overlap_tile8(sprite8, location7):
    if controller.B.is_pressed():
        tiles.set_wall_at(location7, False)
        tiles.set_tile_at(location7, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Log
        """),
    on_overlap_tile8)

def on_overlap_tile9(sprite7, location6):
    if controller.B.is_pressed():
        tiles.set_wall_at(location6, False)
        tiles.set_tile_at(location6, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Log with leaves
        """),
    on_overlap_tile9)

def on_menu_pressed():
    global Menu, Inventory
    Menu = not (Menu)
    if Menu:
        controller.move_sprite(Steve, 0, 0)
        Inventory = miniMenu.create_menu(miniMenu.create_menu_item("Stone", assets.tile("""
                Stone
                """)),
            miniMenu.create_menu_item("Grass", assets.tile("""
                Grass
                """)),
            miniMenu.create_menu_item("Dirt", assets.tile("""
                Dirt
                """)),
            miniMenu.create_menu_item("Log", assets.tile("""
                Log
                """)),
            miniMenu.create_menu_item("Leaves", assets.tile("""
                Leaves
                """)),
            miniMenu.create_menu_item("Log with leaves",
                assets.tile("""
                    Log with leaves
                    """)),
            miniMenu.create_menu_item("Planks", assets.tile("""
                Planks
                """)),
            miniMenu.create_menu_item("Diamond ore", assets.tile("""
                Diamond ore
                """)),
            miniMenu.create_menu_item("Glass", assets.tile("""
                Glass
                """)),
            miniMenu.create_menu_item("Iron ore", assets.tile("""
                Iron ore
                """)),
            miniMenu.create_menu_item("Coal ore", assets.tile("""
                Coal ore
                """)),
            miniMenu.create_menu_item("Bedrock", assets.tile("""
                Bedrock
                """)))
        Inventory.set_stay_in_screen(True)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.ROWS, 3)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.COLUMNS, 5)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.BACKGROUND_COLOR, 1)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.BORDER, 1)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.BORDER_COLOR, 11)
        Inventory.set_style_property(miniMenu.StyleKind.DEFAULT_AND_SELECTED,
            miniMenu.StyleProperty.ICON_ONLY,
            1)
        Inventory.set_style_property(miniMenu.StyleKind.SELECTED,
            miniMenu.StyleProperty.BACKGROUND,
            9)
        Inventory.set_style_property(miniMenu.StyleKind.TITLE,
            miniMenu.StyleProperty.FOREGROUND,
            15)
        Inventory.set_style_property(miniMenu.StyleKind.TITLE,
            miniMenu.StyleProperty.BORDER,
            miniMenu.create_border_box(0, 0, 0, 2))
        Inventory.set_style_property(miniMenu.StyleKind.TITLE,
            miniMenu.StyleProperty.BACKGROUND,
            1)
        Inventory.set_style_property(miniMenu.StyleKind.TITLE,
            miniMenu.StyleProperty.BORDER_COLOR,
            11)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.WIDTH, 102)
        Inventory.set_menu_style_property(miniMenu.MenuStyleProperty.HEIGHT, 73)
        Inventory.bottom = 100
        Inventory.left = 30
        Inventory.set_title("Grass")
        
        def on_selection_changed(selection, selectedIndex):
            Inventory.set_title(selection)
        Inventory.on_selection_changed(on_selection_changed)
        
        
        def on_button_pressed(selection2, selectedIndex2):
            global Block, Block_name
            Block = Block_list[selectedIndex2]
            Block_name = selection2
            Init_hotbar()
            Inventory.close()
        Inventory.on_button_pressed(controller.A, on_button_pressed)
        
        Inventory.set_position(Steve.x, Steve.y)
    else:
        Inventory.close()
        controller.move_sprite(Steve, 100, 100)
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_down_pressed():
    global Down
    Down = True
    Cursor.set_position(Steve.x, Steve.y + 24)
    Down = False
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_up_pressed():
    global Up
    Up = True
    Cursor.set_position(Steve.x, Steve.y - 32)
    Up = False
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile10(sprite, location):
    if controller.B.is_pressed():
        tiles.set_wall_at(location, False)
        tiles.set_tile_at(location, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Grass
        """),
    on_overlap_tile10)

def on_right_pressed():
    global Cursor_left
    Steve.set_image(assets.image("""
        Steve right
        """))
    Cursor_left = False
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def Respawn_slime():
    global Slime
    if Math.percent_chance(50):
        Slime = sprites.create(assets.image("""
            Slime
            """), SpriteKind.Monster)
        tiles.place_on_random_tile(Slime, assets.tile("""
            transparency16
            """))
        Slime.set_velocity(0, 100)
        pause(300)
        for index in range(5):
            if Slime.x < Steve.x:
                Slime.set_velocity(100, -70)
                pause(250)
                Slime.set_velocity(0, 100)
            else:
                Slime.set_velocity(-100, -70)
                pause(250)
                Slime.set_velocity(0, 100)
            pause(randint(1000, 2000))
    else:
        Slime = sprites.create(assets.image("""
            Slime big
            """), SpriteKind.Monster)
        tiles.place_on_random_tile(Slime, assets.tile("""
            transparency16
            """))
        Slime.set_velocity(0, 100)
        pause(300)
        for index2 in range(5):
            if Slime.x < Steve.x:
                Slime.set_velocity(100, -70)
                pause(250)
                Slime.set_velocity(0, 100)
            else:
                Slime.set_velocity(-100, -70)
                pause(250)
                Slime.set_velocity(0, 100)
            pause(randint(1000, 2000))

def on_overlap_tile11(sprite9, location8):
    if controller.B.is_pressed():
        tiles.set_wall_at(location8, False)
        tiles.set_tile_at(location8, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Dirt
        """),
    on_overlap_tile11)

def on_add_handler_update_priority_modifier_after_camera():
    Hotbar.set_position(80, 110)
spriteutils.add_event_handler(spriteutils.UpdatePriorityModifier.AFTER,
    spriteutils.UpdatePriority.CAMERA,
    on_add_handler_update_priority_modifier_after_camera)

def on_left_pressed():
    global Cursor_left
    Steve.set_image(assets.image("""
        Steve left
        """))
    Cursor_left = True
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile12(sprite6, location5):
    if controller.B.is_pressed():
        tiles.set_wall_at(location5, False)
        tiles.set_tile_at(location5, assets.tile("""
            transparency16
            """))
        music.play(music.create_song(assets.song("""
                Break0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        Bedrock
        """),
    on_overlap_tile12)

def on_overlap_tile13(sprite4, location3):
    if controller.A.is_pressed():
        tiles.set_wall_at(location3, True)
        tiles.set_tile_at(location3, Block)
        music.play(music.create_song(assets.song("""
                Place
                """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.cursor,
    assets.tile("""
        transparency16
        """),
    on_overlap_tile13)

def Init_hotbar():
    global Hotbar
    Hotbar = miniMenu.create_menu(miniMenu.create_menu_item(Block_name, Block))
    Hotbar.set_style_property(miniMenu.StyleKind.ALL, miniMenu.StyleProperty.ICON_ONLY, 1)
    Hotbar.set_menu_style_property(miniMenu.MenuStyleProperty.ROWS, 1)
    Hotbar.set_menu_style_property(miniMenu.MenuStyleProperty.COLUMNS, 1)
    Hotbar.set_menu_style_property(miniMenu.MenuStyleProperty.BACKGROUND_COLOR, 1)
    Hotbar.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    Hotbar.set_flag(SpriteFlag.GHOST_THROUGH_TILES, True)
    Hotbar.set_stay_in_screen(True)
    Hotbar.set_position(80, 110)
Hotbar: miniMenu.MenuSprite = None
Slime: Sprite = None
Inventory: miniMenu.MenuSprite = None
Night = False
Up = False
Down = False
Block_name = ""
Block: Image = None
Menu = False
Cursor_left = False
Cursor: Sprite = None
Block_list: List[Image] = []
Tile_map_list: List[tiles.TileMapData] = []
Steve: Sprite = None
Def_list()
Init_start()
Init_hotbar()
controller.move_sprite(Steve, 100, 100)

def on_forever():
    if Night:
        pause(randint(500, 1500))
forever(on_forever)

def on_forever2():
    if Cursor_left and Down == False:
        Cursor.set_position(Steve.x - 16, Steve.y + 8)
    else:
        Cursor.set_position(Steve.x + 16, Steve.y + 8)
    Inventory.set_position(Steve.x, Steve.y)
    Steve.set_velocity(0, 50)
forever(on_forever2)

def on_forever3():
    if Night:
        scene.set_background_color(13)
    else:
        scene.set_background_color(15)
forever(on_forever3)

def on_forever4():
    global Night
    pause(60000)
    Night = not (Night)
    pause(60000)
    Night = not (Night)
forever(on_forever4)
