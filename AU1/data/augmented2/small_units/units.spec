
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
	XYZ,
	VladimirSlavik,
	Wahazar
	Kinboat
	Wahazar
	Wyrmshadow 
"
;copy of trident units with exceptions
[file]
gfx = "trident/units"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 30
dy = 30

tiles = { "row", "column", "tag"

  0,  0, "u.armor"
  0,  1, "u.howitzer"
  0,  2, "u.battleship"
  0,  3, "u.bomber"
  0,  4, "u.cannon"
  0,  5, "u.caravan"
  0,  6, "u.carrier"
  0,  7, "u.catapult"
  0,  8, "u.horsemen"
  0,  9, "u.chariot"
  0, 10, "u.cruiser"
  0, 11, "u.diplomat", "u.barbarian_leader"
  0, 12, "u.fighter"
  0, 13, "u.frigate"
  0, 14, "u.ironclad"
  0, 15, "u.knights"
  0, 16, "u.legion"
  0, 17, "u.mech_inf"
  0, 18, "u.warriors"
  0, 19, "u.musketeers"
;  1,  0, "u.nuclear"
  1,  1, "u.phalanx"
  1,  2, "u.riflemen"
  1,  3, "u.caravel"
  1,  4, "u.settlers"
  1,  5, "u.submarine"
  1,  6, "u.transport"
  1,  7, "u.trireme"
  1,  8, "u.archers"
  1,  9, "u.cavalry"
;  1, 10, "u.cruise_missile"
  1, 11, "u.destroyer"
  1, 12, "u.dragoons"
  1, 13, "u.explorer"
  1, 14, "u.freight"
  1, 15, "u.galleon"
  1, 16, "u.partisan"
  1, 17, "u.pikemen"
  2,  0, "u.marines"
  2,  1, "u.spy"
  2,  2, "u.engineers"
  2,  3, "u.artillery"
  2,  4, "u.helicopter"
  2,  5, "u.alpine_troops"
  2,  6, "u.stealth_bomber"
  2,  7, "u.stealth_fighter"
  2,  8, "u.aegis_cruiser"
  2,  9, "u.paratroopers"
  2, 10, "u.elephants"
  2, 11, "u.crusaders"
  2, 12, "u.fanatics"
  2, 13, "u.awacs"
  2, 14, "u.worker"
  2, 15, "u.leader"
  2, 16, "u.migrants"
}

[extra]
sprites =
	{	"tag", "file"
		"u.mg_infantry", "augmented2/small_units/mg_infantry_t"
		"u.rpg_infantry", "augmented2/small_units/rpg_infantry_t"
		"u.railgun_destroyer", "augmented2/small_units/zumwalt_t"
		"u.autonomous_war_mech", "augmented2/small_units/warmech_t"
		"u.super_soldiers", "augmented2/small_units/super_soldiers_t"
		"u.drone", "augmented2/small_units/drone_t"
		"u.antimatter_fighter", "augmented2/small_units/antimatter_fighter_t"
		"u.antimatter_bomber", "augmented2/small_units/antimatter_bomber_t"
		"u.jet_fighter", "augmented2/small_units/Mig3"
		"u.technical", "augmented2/small_units/technical-trident-transparent"
		"u.balloon", "augmented2/small_units/Balloon5"
		"u.anti_aircraft_gun", "augmented2/small_units/Gepard-Flakpanzer-brighter"
		"u.arquebusiers", "augmented2/small_units/arquebusiers_t"
		"u.marksman", "augmented2/small_units/Marksman9"
		"u.line_infantry", "augmented2/small_units/line_infantry_t"
		"u.halberdier", "augmented2/small_units/halberdier6"
		"u.train", "augmented2/small_units/locomotive-trident-transparent"
		"u.sniper", "augmented2/small_units/sniper_t"
		"u.arbalest", "augmented2/small_units/Arbalest6"
		"u.grenadier", "augmented2/small_units/grenadier_t"
		"u.stormtrooper", "augmented2/small_units/Stormtrooper16"
		"u.turret_cannon", "augmented2/small_units/turret_cannon_t"
		"u.turret_aa_gun", "augmented2/small_units/turret_aa_gun_t"
		"u.torpedo", "augmented2/small_units/torpedo_t"
		"u.armoured_train", "augmented2/small_units/Armouredtrain11"
		"u.self_propelled_gun", "augmented2/small_units/self_propelled_gun_t"
		"u.reactive_armor", "augmented2/small_units/reactive_armor_t"
		"u.bombard", "augmented2/small_units/bombard_t"
		"u.gun_howitzer", "augmented2/small_units/gun_howitzer_t"
		"u.ballista", "augmented2/small_units/ballista_t"
		"u.galley", "augmented2/small_units/galley_t"
		"u.cog", "augmented2/small_units/cog_t"
		"u.monitor", "augmented2/small_units/monitor_t"
		"u.paddle_steamer", "augmented2/small_units/paddle_steamer_t"
		"u.patrol_boat", "augmented2/small_units/patrol_boat_t"
		"u.steam_barge", "augmented2/small_units/steam_barge_t"
		"u.diesel_barge", "augmented2/small_units/diesel_barge_t"
		"u.vikings", "augmented2/small_units/viking_t"
		"u.longboat", "augmented2/small_units/Longship3"
		"u.corsairs", "augmented2/small_units/corsair_t"
		"u.battering_ram", "augmented2/small_units/battering_ram_t"
		"u.aak", "augmented2/small_units/Aak_t"
		"u.raft", "augmented2/small_units/raft_t"
		"u.Abomb", "augmented2/small_units/Abomb_t"
		"u.GBU", "augmented2/small_units/GBU_t"
		"u.zeppelin", "augmented2/small_units/zeppelin_t"
		"u.airplane", "augmented2/small_units/airplane_t"
		"u.strike_aircraft", "augmented2/small_units/strike_aircraft_t"
		"u.nuclear_submarine", "augmented2/small_units/nuclear_submarine_t"
		"u.strike_jet", "augmented2/small_units/strike_jet_t"
		"u.riot_police", "augmented2/small_units/riot_police_t"
		"u.navy_seals", "augmented2/small_units/navy_seals_t"
		"u.slave", "augmented2/small_units/slave_t"
		"u.messenger", "augmented2/small_units/messenger_t"
		"u.mounted_samurai", "augmented2/small_units/mounted_samurai_t"
		"u.samurai", "augmented2/small_units/samurai_t"
		"u.junk", "augmented2/small_units/junk_t"
		"u.mounted_archery", "augmented2/small_units/mounted_archery_t"
		"u.dromedari", "augmented2/small_units/dromedari_t"
		"u.janissaries", "augmented2/small_units/janissaries_t"
		"u.AT-gun", "augmented2/small_units/AT-gun_t"
		"u.ninja", "augmented2/small_units/ninja_t"
		"u.tribe", "augmented2/small_units/tribe_t"
		"u.hunters", "augmented2/small_units/hunters_t"
		"u.canoes", "augmented2/small_units/canoes_t"
		"u.swordsmen", "augmented2/small_units/swordsmen_t"
		"u.crusaders_horse", "augmented2/small_units/crusaders_horse_t"
		"u.bicycle_infantry", "augmented2/small_units/bicycle_infantry_t"
		"u.mounted_inf", "augmented2/small_units/mounted_inf_t"
		"u.lancers", "augmented2/small_units/lancers_t"
		"u.dragoon", "augmented2/small_units/dragoon_t"
		"u.militia", "augmented2/small_units/militia_t"
		"u.missile", "augmented2/small_units/missile_t"
		"u.armor_car", "augmented2/small_units/armor_car_t"
		"u.atv_infantry", "augmented2/small_units/ATV_infantry_t"
		"u.flagship_frigate", "augmented2/small_units/Flagship2"
		"u.builder", "augmented2/small_units/builders_t"
		"u.clipper", "augmented2/small_units/clipper_t"
		"u.freighter", "augmented2/small_units/freighter_t"
		"u.jetliner", "augmented2/small_units/jetliner_t"
		"u.brig", "augmented2/small_units/brig_t"
		"u.pirates_brig", "augmented2/small_units/pirates_brig_t"
		"u.kon-tiki_raft", "augmented2/small_units/kon-tiki_raft_t"
		"u.tactical_abm", "augmented2/small_units/patriot-trident"
		"u.streltsy", "augmented2/small_units/streltsy_t"
		"u.hovercraft", "augmented2/small_units/hovercraft_t"
		"u.skirmishers", "augmented2/small_units/skirmishers_t"
		"u.pirates", "augmented2/small_units/pirates_t"
		"u.scout", "augmented2/small_units/scout_t"
		"u.wagenburg", "augmented2/small_units/wagenburg_t"
		"u.floating_bridge", "augmented2/small_units/floating_bridge_srb"
		"u.cart", "augmented2/small_units/cart_t"
; swapped standard graphics
		"u.direct_artillery", "augmented2/small_units/direct_artillery_t"
		"u.plunging_cannon", "augmented2/small_units/plunging_cannon_t"
		"u.musketeer", "augmented2/small_units/musketeer_t"
		"u.nuclear", "augmented2/small_units/nuclear_t"
		"u.cruise_missile", "augmented2/small_units/cruise_missile_t"
	}

