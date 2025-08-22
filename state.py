from highscore import load_high_score
class GameState:
    def __init__(self):

        #General#################################
        self.points = 0
        self.life_no = 3
        self.game_over = False
        self.respawn = False
        self.wave_time = 35    #default 35
        self.breaktime = 4
        self.life_milestone = 3000
        self.life_milestone_intervall = 3000
        self.high_score = load_high_score()
        self.new_high_score = False
        self.MAX_LIFE = 5
        self.level_break = False
        self.level_active = True
        self.pause_active = False
        self.last_pause_push = 0
        self.level = 1     #default 1
        self.all_death = False
        self.boss_level = False
        self.joysticks = 0
        self.boost_active = False
        self.player_acceleration = 350
        self.selector_position = 1
        self.start_rumble = 0
        #Virus###################################
        self.virus_speed = 12
        self.max_virus_spawn = 4
        self.speed_safe = 12
        self.speed_restore = 12
        #self.virus_count = 2
        self.virus_freq = 500 / 1000
        self.last_virus_spawn = 0
        self.last_virus2_spawn = 0
        self.virus2_freq = 10000/1000
        self.virus_speed_increase = 5         #increase default 2.5
        self.new_viruses = True
        # BOSS#######################
        self.target_pos = [100,100]
        self.boss_hp = 500
        #Power UP and ammo#######################
        self.pup_speed = 10
        self.pup_blink = False
        self.pup_frequency = 20
        self.pup_timer_visible = 0
        self.pup_timer_visible_default = 18
        self.pup_active = False
        self.pup_from = 1
        self.pup_to = 6
        self.ammo_type = 1
        self.last_shot_time = 0
        self.shot_frequency = .300
        self.max_shots = 2
        self.power_up_timer = 0
        self.damage = 6
        self.damage_default = 6
        self.pup_type = 1
        self.pup_life = 2
        self.last_pup_spawn = 0
        self.dual_shot = False
        self.vacc_speed = 300
        self.vacc_speed_default = 300
    # SHIELD ############################################## ##
        self.energy_level = 20
        #self.shield_life_default = 20
        self.additional_energy = 20
        self.shield_blink = False
        self.shield_active = False
    # INPUT HANDLING ########################################
        self.PAUSE_KEY = False


