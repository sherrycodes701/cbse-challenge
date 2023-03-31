namespace SpriteKind {
    export const Tree = SpriteKind.create()
}
function makeAllTrees () {
    tree1 = sprites.create(, SpriteKind.Tree)
    tree1.setPosition(13, 16)
    tree2 = sprites.create(, SpriteKind.Tree)
    tree2.setPosition(65, 16)
    tree3 = sprites.create(, SpriteKind.Tree)
    tree3.setPosition(129, 16)
    tree4 = sprites.create(, SpriteKind.Tree)
    tree4.setPosition(12, 52)
    tree5 = sprites.create(, SpriteKind.Tree)
    tree5.setPosition(53, 55)
    tree6 = sprites.create(, SpriteKind.Tree)
    tree6.setPosition(93, 63)
    tree7 = sprites.create(, SpriteKind.Tree)
    tree7.setPosition(140, 63)
    tree8 = sprites.create(, SpriteKind.Tree)
    tree8.setPosition(29, 91)
    tree9 = sprites.create(, SpriteKind.Tree)
    tree9.setPosition(65, 93)
    tree10 = sprites.create(, SpriteKind.Tree)
    tree10.setPosition(123, 94)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (level == 0) {
        info.setLife(8)
        level += 1
    }
    if (level == 1) {
        for (let value of list) {
            let mySprite: Sprite = null
            cutTree(mySprite)
        }
    }
})
function cutTree (mySprite: Sprite) {
    sprites.destroy(mySprite)
    info.changeLifeBy(-1)
}
info.onLifeZero(function () {
    game.gameOver(false)
    game.setGameOverPlayable(false, music.melodyPlayable(music.bigCrash), false)
    game.setGameOverMessage(false, "GAME OVER!")
})
let tree10: Sprite = null
let tree9: Sprite = null
let tree8: Sprite = null
let tree7: Sprite = null
let tree6: Sprite = null
let tree5: Sprite = null
let tree4: Sprite = null
let tree3: Sprite = null
let tree2: Sprite = null
let tree1: Sprite = null
let level = 0
let list = 0
list = 0
level = 0
game.splash("Welcome to The UNIVERSAL PROGRAMMERS!")
scene.setBackgroundImage()
makeAllTrees()
