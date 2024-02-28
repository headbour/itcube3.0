import pygame

score = 0
bg_x = 0
clock = pygame.time.Clock()
player_speed = 10
player_x = 150
player_y = 400
naves_puli = True
cactus_x = 1300
coeficent_slojnosti = 1
is_jump = False
jump_count = 11

pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Pobeg')
icon = pygame.image.load(r"data\icon.png")
bg_start = pygame.image.load(r"data\nacalni_ecran.jpg")
pygame.display.set_icon(icon)
zvuk_vzriva = pygame.mixer.Sound(r'data\vzriv.mp3')
bg_musik = pygame.mixer.Sound(r'data\musik.mp3')
bg_musik.play()
jump = pygame.mixer.Sound(r'data\jump.mp3')
run = pygame.mixer.Sound(r'data\run.mp3')

sd = 0
fon = pygame.image.load(r'data\bgg.png').convert()
bg = pygame.image.load(r'data\bgg1.png').convert_alpha()
cactus = pygame.image.load(r'data\cactus.png').convert_alpha()
bullet = pygame.image.load(r'data\dinamit.png').convert_alpha()
# bg2 = pygame.image.load('bgg2.png')
player = pygame.image.load(r'data\hero_pravo1.png').convert_alpha()
police = pygame.image.load(r'data\police.png').convert_alpha()
magazin0 = pygame.image.load(r'data\magazin0.png').convert_alpha()
magazin1 = pygame.image.load(r'data\magazin1.png').convert_alpha()
magazin2 = pygame.image.load(r'data\magazin2.png').convert_alpha()
magazin3 = pygame.image.load(r'data\magazin3.png').convert_alpha()
police_x = 2000
colorkey = player.get_at((0, 0))
player.set_colorkey(colorkey)
player1 = [pygame.image.load(r'data\hero_pravo1.png').convert_alpha(),
           pygame.image.load(r'data\hero_pravo2.png').convert_alpha(),
           pygame.image.load(r'data\hero_pravo3.png').convert_alpha(),
           pygame.image.load(r'data\hero_pravo4.png').convert_alpha(),
           pygame.image.load(r'data\hero_pravo5.png').convert_alpha(),
           ]

player_anim_count = 0
bg_x = 0

running = True

police_timer = pygame.USEREVENT + 1
pygame.time.set_timer(police_timer, 5000)
police_list_in_game = []

nacalni_ecran = False
gameplay = True
fon_smerti = pygame.image.load(r'data\fon_proigrisha.jpg')

label = pygame.font.Font(r'data\shrift.ttf', 140)
label1 = pygame.font.Font(r'data\shrift1.otf', 100)
label2 = pygame.font.Font(r'data\shrift1.otf', 90)
score_label1 = pygame.font.Font(r'data\shrift1.otf', 90)
lose_label = label.render(r'You Lose!', False, (0, 0, 0))
score_label = score_label1.render('Score:' + str(score), False, (0, 0, 0))
newgame_label = label1.render(r'Restart', False, (0, 0, 0))
back_to_game = label2.render(r'back to menu', False, (0, 0, 0))
newgame_label_rect = newgame_label.get_rect(topleft=(300, 260))
back_to_game_label_rect = newgame_label.get_rect(topleft=(230, 350))

play_label_rect = newgame_label.get_rect(topleft=(900, 60))

bullets = []
dinamit_y = 0
dinamits = 3

while running:
    clock.tick(15)

    if nacalni_ecran:
        if gameplay:
            for i in range(100):
                screen.blit(bg, (bg_x + 2483 * i, 50))

            screen.blit(cactus, (bg_x + 2000, 450))
            screen
            if coeficent_slojnosti <= 3:

                bg_x -= a
                if police_list_in_game:
                    for (i, el) in enumerate(police_list_in_game):
                        screen.blit(police, el)

                        if el.x < -100:
                            police_list_in_game.pop(i)
            else:
                a = 20 * coeficent_slojnosti
                bg_x -= a
            if police_list_in_game:
                for (i, el) in enumerate(police_list_in_game):
                    screen.blit(police, el)

                    if el.x < -100:
                        police_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    print('fff')
                    gameplay = False

            screen.blit(player1[player_anim_count], (player_x, player_y))
            player_rect = player1[0].get_rect(topleft=(player_x, player_y))

            player_anim_count += 1
            if player_anim_count == 5:
                player_anim_count = 1
            if not is_jump and sd == 1:
                run.play()

            sd += 1
            if sd == 5:
                sd = 0

            keys = pygame.key.get_pressed()
            if not is_jump:
                if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -11:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    jump.play()
                    is_jump = False
                    jump_count = 11

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x + 50, el.y - 100))
                    el.x += 20
                    el.y += 2
                    if el.y >= 500:
                        zvuk_vzriva.play()
                        bullets.pop(i)
                    if police_list_in_game:
                        for (index, police_el) in enumerate(police_list_in_game):
                            if el.colliderect(police_el):
                                police_list_in_game.pop(index)
                                bullets.pop(i)
                                zvuk_vzriva.play()
            if dinamits == 3:
                screen.blit(magazin3, (0, 50))
            elif dinamits == 2:
                screen.blit(magazin2, (0, 50))
            elif dinamits == 1:
                screen.blit(magazin1, (0, 50))
            elif dinamits < 1:
                screen.blit(magazin0, (0, 50))
        else:
            screen.blit(fon_smerti, (0, 0))
            screen.blit(lose_label, (140, 100))
            screen.blit(newgame_label, newgame_label_rect)
            screen.blit(back_to_game, back_to_game_label_rect)
            mouse = pygame.mouse.get_pos()
            if newgame_label_rect.collidepoint(mouse):
                newgame_label = label1.render('Restart', False, (128, 0, 0))
            else:
                newgame_label = label1.render('Restart', False, (0, 0, 0))

            if newgame_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 150
                police_list_in_game.clear()
                bullets.clear()
                dinamits = 3

            if back_to_game_label_rect.collidepoint(mouse):
                back_to_game = label2.render('back to menu', False, (128, 0, 0))
            else:
                back_to_game = label2.render('back to menu', False, (0, 0, 0))
            if back_to_game_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                nacalni_ecran = False
                gameplay = True
                dinamits = 3
                player_x = 150
                police_list_in_game.clear()
                bullets.clear()
    else:
        screen.blit(bg_start, (0, -200))
        mouse = pygame.mouse.get_pos()
        screen.blit(newgame_label, play_label_rect)
        if play_label_rect.collidepoint(mouse):
            newgame_label = label1.render('Play!', False, (128, 0, 0))
        else:
            newgame_label = label1.render('Play!', False, (0, 0, 0))

        if play_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            nacalni_ecran = True
            dinamits = 3
            player_x = 150
            police_list_in_game.clear()
            bullets.clear()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == police_timer:
            police_list_in_game.append(police.get_rect(topleft=(2000, 560)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_e and dinamits > 0:
            bullets.append(bullet.get_rect(topleft=(player_x, player_y)))
            dinamits -= 1
