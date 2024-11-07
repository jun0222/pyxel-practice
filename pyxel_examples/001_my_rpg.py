import pyxel

class SimpleRPG:
    def __init__(self):
        pyxel.init(160, 120, title="RPG with Events")
        
        # マップデータ (0: 空地, 1: 壁, 2: NPC)
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # プレイヤー、NPC、イベントの初期位置
        self.player_x = 80
        self.player_y = 60
        self.npc_x = 40
        self.npc_y = 60
        self.event_triggered = False  # イベント発生フラグ
        # self.message = "Welcome to the RPG world!"
        self.message = ""
        self.event_step = 0  # イベントの進行ステップ
        
        pyxel.run(self.update, self.draw)

    def update(self):
        # イベントが発生していなければプレイヤーを移動可能
        if not self.event_triggered:
            self.move_player()
            self.check_for_event_trigger()
        else:
            # イベントが発生している場合はイベントを処理
            self.handle_event()

    def move_player(self):
        new_x = self.player_x
        new_y = self.player_y
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            new_x = min(self.player_x + 2, 160)
        if pyxel.btn(pyxel.KEY_LEFT):
            new_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_UP):
            new_y = max(self.player_y - 2, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            new_y = min(self.player_y + 2, 120)
        
        # マップの境界チェック
        if self.map_data[new_y // 8][new_x // 8] == 0:
            self.player_x = new_x
            self.player_y = new_y

    def check_for_event_trigger(self):
        # NPCとの接触チェック
        if abs(self.player_x - self.npc_x) < 8 and abs(self.player_y - self.npc_y) < 8:
            self.event_triggered = True
            self.message = "You met an NPC!"

    def handle_event(self):
        # イベントの処理
        self.event_step += 1
        if self.event_step > 30:
            self.event_triggered = False
            self.event_step = 0
            # self.message = "Welcome to the RPG world!"
            self.message = ""

    def draw(self):
        pyxel.cls(0)
        self.draw_map()
        pyxel.rect(self.player_x, self.player_y, 8, 8, 9)  # プレイヤーを描画
        pyxel.rect(self.npc_x, self.npc_y, 8, 8, 8)  # NPCを描画
        pyxel.text(5, 5, self.message, pyxel.frame_count % 16)

    def draw_map(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    pyxel.rect(x * 8, y * 8, 8, 8, 7)  # 壁を描画
                elif tile == 2:
                    pyxel.rect(x * 8, y * 8, 8, 8, 8)  # NPCを描画

SimpleRPG()