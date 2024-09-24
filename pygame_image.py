import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像の読み込み
    bg_img = pg.image.load("fig/pg_bg.jpg")
    # こうかとん画像の読み込み
    koukaton_img = pg.image.load("fig/3.png")
    # こうかとん画像の左右反転
    koukaton_img = pg.transform.flip(koukaton_img, True, False)

    bg_x = 0  # 背景の横座標を初期化

    while True:
        for event in pg.event.get():  # ウィンドウを閉じることを許可する
            if event.type == pg.QUIT:
                return

        # 背景画像の移動
        bg_x -= 1  # 左に移動
        if bg_x <= -1600:  # 800フレーム進んだらリセット（画像幅の半分）
            bg_x = 0

        # 背景を描画
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_img, [bg_x + 1600, 0])  # 右側の背景も描画（間延び防止）

        # こうかとんを描画
        screen.blit(koukaton_img, [300, 200])

        pg.display.update()
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
