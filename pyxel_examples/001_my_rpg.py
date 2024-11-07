import pyxel

class SimpleRPG:
    def __init__(self):
        pyxel.init(160, 120, title="RPG with Events")
        
        # プレイヤー、NPC、イベントの初期位置
        self.player_x = 80
        self.player_y = 60
        self.npc_x = 40
        self.npc_y = 60
        self.event_triggered = False  # イベント発生フラグ
        self.message = "Welcome to the RPG world!"
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
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, 160)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_UP):
            self.player_y = max(self.player_y - 2, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player_y = min(self.player_y + 2, 120)

    def check_for_event_trigger(self):
        # NPCと接触した場合にイベントを開始
        if abs(self.player_x - self.npc_x) < 8 and abs(self.player_y - self.npc_y) < 8:
            self.event_triggered = True
            self.message = "NPC: Let's go to the next area!"
            self.event_step = 0  # イベント進行の初期化

    def handle_event(self):
        # イベントの進行状況に応じた処理
        if self.event_step == 0:
            # NPCが移動を開始
            self.npc_x += 1
            if self.npc_x > 100:  # ある位置まで移動したら次のステップ
                self.event_step = 1
                self.message = "NPC: Follow me!"
        elif self.event_step == 1:
            # プレイヤーがNPCを追うフェーズ
            if abs(self.player_x - self.npc_x) < 8 and abs(self.player_y - self.npc_y) < 8:
                self.event_step = 2
                self.message = "NPC: We've arrived!"
        elif self.event_step == 2:
            # イベント終了
            self.message = "The event is over. Explore the world!"
            self.event_triggered = False

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, self.message, 7)
        
        # プレイヤーの描画
        pyxel.rect(self.player_x, self.player_y, 8, 8, 11)

        # NPCの描画
        pyxel.circ(self.npc_x, self.npc_y, 6, 10)

# ゲーム開始
SimpleRPG()
