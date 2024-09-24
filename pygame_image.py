import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    
    kk_img = pg.image.load("fig/3.png")  # 練習２
    kk_img = pg.transform.flip(kk_img, True, False)  # 練習２
    kk_rct = kk_img.get_rect()  # 練習8-1：SurfaceからRectを抽出する
    kk_rct.center = 300, 200  # 練習8-2：Rectを使った初期座標の設定
    
    tmr = 0
    bg_speed = 1  # 背景の初期速度

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_lst = pg.key.get_pressed()  # 練習8-3：キーの押下状態を取得

        # こうかとんの移動処理
        if key_lst[pg.K_UP]:  # 上矢印キーがTrueなら
            kk_rct.move_ip(0, -1)  # こうかとんの縦座標を-1する
        if key_lst[pg.K_DOWN]:  # 下矢印キーがTrueなら
            kk_rct.move_ip(0, +1)  # こうかとんの縦座標を+1する
        if key_lst[pg.K_LEFT]:  # 左矢印キーがTrueなら
            kk_rct.move_ip(-1, 0)  # こうかとんの横座標を-1する
        if key_lst[pg.K_RIGHT]:  # 右矢印キーがTrueなら
            kk_rct.move_ip(+2, 0)  # こうかとんの横座標を+1する

        else:
            kk_rct.move_ip(-1, 0)  # それ以外は通常速度

        # 背景の移動処理
        x = -(tmr * bg_speed % 3200)  # 倍速対応で背景を左に流す
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bg_img2, [x + 4800, 0])

        # こうかとんの描画
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1        
        clock.tick(200)  # 練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
