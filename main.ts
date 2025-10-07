namespace SpriteKind {
    export const cursor = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Log`, function (sprite8, location7) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location7, false)
        tiles.setTileAt(location7, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Grass`, function (sprite, location) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location, false)
        tiles.setTileAt(location, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
spriteutils.addEventHandler(spriteutils.UpdatePriorityModifier.After, spriteutils.UpdatePriority.Camera, function () {
    Hotbar.setPosition(80, 110)
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Stone`, function (sprite12, location11) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location11, false)
        tiles.setTileAt(location11, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break`), music.PlaybackMode.InBackground)
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    Up = true
    Cursor.setPosition(Steve.x, Steve.y - 32)
    Up = false
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Bedrock`, function (sprite6, location5) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location5, false)
        tiles.setTileAt(location5, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    Steve.setImage(assets.image`Steve left`)
    Cursor_left = true
})
function Def_list () {
    Tile_map_list = [
    tilemap`World 1`,
    tilemap`World 2`,
    tilemap`World 3`,
    tilemap`World 4`,
    tilemap`World 5`,
    tilemap`World 6`,
    tilemap`World 7`,
    tilemap`World 8`,
    tilemap`World 9`,
    tilemap`Superflat`
    ]
    Block_list = [
    assets.tile`Stone`,
    assets.tile`Grass`,
    assets.tile`Dirt`,
    assets.tile`Log`,
    assets.tile`Leaves`,
    assets.tile`Log with leaves`,
    assets.tile`Planks`,
    assets.tile`Diamond ore`,
    assets.tile`Glass`,
    assets.tile`Iron ore`,
    assets.tile`Coal ore`,
    assets.tile`Bedrock`
    ]
}
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Log with leaves`, function (sprite7, location6) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location6, false)
        tiles.setTileAt(location6, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
sprites.onOverlap(SpriteKind.cursor, SpriteKind.Enemy, function (sprite2, otherSprite) {
    if (controller.B.isPressed()) {
        music.play(music.createSong(assets.song`Hit`), music.PlaybackMode.InBackground)
        sprites.destroy(otherSprite, effects.disintegrate, 500)
        info.changeScoreBy(1)
        Respawn_slime()
    }
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Leaves`, function (sprite5, location4) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location4, false)
        tiles.setTileAt(location4, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
function Init_start () {
    tiles.setCurrentTilemap(Tile_map_list._pickRandom())
    Steve = sprites.create(assets.image`Steve right`, SpriteKind.Player)
    scene.cameraFollowSprite(Steve)
    Steve.setStayInScreen(true)
    Steve.setFlag(SpriteFlag.GhostThroughSprites, false)
    Cursor = sprites.create(assets.image`Cursor`, SpriteKind.cursor)
    Cursor.setFlag(SpriteFlag.GhostThroughWalls, true)
    Cursor_left = false
    Menu = false
    Block = assets.tile`Grass`
    Block_name = "Grass"
    Down = false
    Up = false
    Night = false
    Inventory = miniMenu.createMenu(
    miniMenu.createMenuItem("Stone", assets.tile`Stone`),
    miniMenu.createMenuItem("Grass", assets.tile`Grass`),
    miniMenu.createMenuItem("Dirt", assets.tile`Dirt`),
    miniMenu.createMenuItem("Log", assets.tile`Log`),
    miniMenu.createMenuItem("Leaves", assets.tile`Leaves`),
    miniMenu.createMenuItem("Log with leaves", assets.tile`Log with leaves`),
    miniMenu.createMenuItem("Planks", assets.tile`Planks`),
    miniMenu.createMenuItem("Diamond ore", assets.tile`Diamond ore`),
    miniMenu.createMenuItem("Glass", assets.tile`Glass`),
    miniMenu.createMenuItem("Iron ore", assets.tile`Iron ore`),
    miniMenu.createMenuItem("Coal ore", assets.tile`Coal ore`),
    miniMenu.createMenuItem("Bedrock", assets.tile`Bedrock`)
    )
    Inventory.close()
    music.setVolume(255)
}
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Diamond ore`, function (sprite10, location9) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location9, false)
        tiles.setTileAt(location9, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
function Jump (Slime: Sprite) {
    if (Slime.x < Steve.x) {
        Slime.setVelocity(100, -70)
        pause(250)
        Slime.setVelocity(0, 100)
    } else {
        Slime.setVelocity(-100, -70)
        pause(250)
        Slime.setVelocity(0, 100)
    }
    pause(randint(1000, 2000))
}
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Iron ore`, function (sprite3, location2) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location2, false)
        tiles.setTileAt(location2, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Glass`, function (sprite13, location12) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location12, false)
        tiles.setTileAt(location12, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    Steve.setImage(assets.image`Steve right`)
    Cursor_left = false
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Coal ore`, function (sprite11, location10) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location10, false)
        tiles.setTileAt(location10, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
function Respawn_slime () {
	
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    Down = true
    Cursor.setPosition(Steve.x, Steve.y + 24)
    Down = false
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    Menu = !(Menu)
    if (Menu) {
        controller.moveSprite(Steve, 0, 0)
        Inventory = miniMenu.createMenu(
        miniMenu.createMenuItem("Stone", assets.tile`Stone`),
        miniMenu.createMenuItem("Grass", assets.tile`Grass`),
        miniMenu.createMenuItem("Dirt", assets.tile`Dirt`),
        miniMenu.createMenuItem("Log", assets.tile`Log`),
        miniMenu.createMenuItem("Leaves", assets.tile`Leaves`),
        miniMenu.createMenuItem("Log with leaves", assets.tile`Log with leaves`),
        miniMenu.createMenuItem("Planks", assets.tile`Planks`),
        miniMenu.createMenuItem("Diamond ore", assets.tile`Diamond ore`),
        miniMenu.createMenuItem("Glass", assets.tile`Glass`),
        miniMenu.createMenuItem("Iron ore", assets.tile`Iron ore`),
        miniMenu.createMenuItem("Coal ore", assets.tile`Coal ore`),
        miniMenu.createMenuItem("Bedrock", assets.tile`Bedrock`)
        )
        Inventory.setStayInScreen(true)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.Rows, 3)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.Columns, 5)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.BackgroundColor, 1)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.Border, 1)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.BorderColor, 11)
        Inventory.setStyleProperty(miniMenu.StyleKind.DefaultAndSelected, miniMenu.StyleProperty.IconOnly, 1)
        Inventory.setStyleProperty(miniMenu.StyleKind.Selected, miniMenu.StyleProperty.Background, 9)
        Inventory.setStyleProperty(miniMenu.StyleKind.Title, miniMenu.StyleProperty.Foreground, 15)
        Inventory.setStyleProperty(miniMenu.StyleKind.Title, miniMenu.StyleProperty.Border, miniMenu.createBorderBox(
        0,
        0,
        0,
        2
        ))
        Inventory.setStyleProperty(miniMenu.StyleKind.Title, miniMenu.StyleProperty.Background, 1)
        Inventory.setStyleProperty(miniMenu.StyleKind.Title, miniMenu.StyleProperty.BorderColor, 11)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.Width, 102)
        Inventory.setMenuStyleProperty(miniMenu.MenuStyleProperty.Height, 73)
        Inventory.bottom = 100
        Inventory.left = 30
        Inventory.setTitle("Grass")
        Inventory.onSelectionChanged(function (selection, selectedIndex) {
            Inventory.setTitle(selection)
        })
        Inventory.onButtonPressed(controller.A, function (selection2, selectedIndex2) {
            Block = Block_list[selectedIndex2]
            Block_name = selection2
            Init_hotbar()
            Inventory.close()
        })
        Inventory.setPosition(Steve.x, Steve.y)
    } else {
        Inventory.close()
        controller.moveSprite(Steve, 100, 100)
    }
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`transparency16`, function (sprite4, location3) {
    if (controller.A.isPressed()) {
        tiles.setWallAt(location3, true)
        tiles.setTileAt(location3, Block)
        music.play(music.createSong(assets.song`Place`), music.PlaybackMode.InBackground)
    }
})
function Random_jump (Slime: Sprite) {
	
}
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Dirt`, function (sprite9, location8) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location8, false)
        tiles.setTileAt(location8, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
scene.onOverlapTile(SpriteKind.cursor, assets.tile`Planks`, function (sprite14, location13) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location13, false)
        tiles.setTileAt(location13, assets.tile`transparency16`)
        music.play(music.createSong(assets.song`Break0`), music.PlaybackMode.InBackground)
    }
})
function Init_hotbar () {
    Hotbar = miniMenu.createMenu(
    miniMenu.createMenuItem(Block_name, Block)
    )
    Hotbar.setStyleProperty(miniMenu.StyleKind.All, miniMenu.StyleProperty.IconOnly, 1)
    Hotbar.setMenuStyleProperty(miniMenu.MenuStyleProperty.Rows, 1)
    Hotbar.setMenuStyleProperty(miniMenu.MenuStyleProperty.Columns, 1)
    Hotbar.setMenuStyleProperty(miniMenu.MenuStyleProperty.BackgroundColor, 1)
    Hotbar.setFlag(SpriteFlag.RelativeToCamera, true)
    Hotbar.setFlag(SpriteFlag.GhostThroughTiles, true)
    Hotbar.setStayInScreen(true)
    Hotbar.setPosition(80, 110)
}
let Inventory: miniMenu.MenuSprite = null
let Night = false
let Down = false
let Block_name = ""
let Block: Image = null
let Menu = false
let Block_list: Image[] = []
let Tile_map_list: tiles.TileMapData[] = []
let Cursor_left = false
let Cursor: Sprite = null
let Up = false
let Hotbar: miniMenu.MenuSprite = null
let Steve: Sprite = null
Def_list()
Init_start()
Init_hotbar()
controller.moveSprite(Steve, 100, 100)
forever(function () {
    if (Cursor_left && Down == false) {
        Cursor.setPosition(Steve.x - 16, Steve.y + 8)
    } else {
        Cursor.setPosition(Steve.x + 16, Steve.y + 8)
    }
    Inventory.setPosition(Steve.x, Steve.y)
    Steve.setVelocity(0, 50)
})
forever(function () {
    pause(60000)
    Night = !(Night)
    pause(60000)
    Night = !(Night)
})
forever(function () {
    if (Night) {
        scene.setBackgroundColor(13)
    } else {
        scene.setBackgroundColor(15)
    }
})
forever(function () {
    if (Night) {
        pause(randint(500, 1500))
    }
})
