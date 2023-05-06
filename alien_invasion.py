import sys,pygame
from setting import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()

        #初始化窗口并设置窗口大小
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        #将screen参数传递给Ship类
        self.ship = Ship(self)
        #设置窗口标题及图标
        pygame.display.set_caption(self.settings.caption)
        pygame.display.set_icon(self.settings.icon)
        #设置背景色

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            #监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #每次循环时都重绘屏幕填充色彩
            self.screen.fill(self.settings.bg_color)
            self.ship.blite()
            #让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实列并运行游戏
    ai = AlienInvasion()
    ai.run_game()