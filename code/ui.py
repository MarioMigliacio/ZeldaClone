import pygame
from settings import *

class UI:
    def __init__(self):
        # surface and font
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        
        # bar setup
        self.health_bar_rect = pygame.Rect(HEALTH_BAR_X, HEALTH_BAR_Y, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(ENERGY_BAR_X, ENERGY_BAR_Y, ENERGY_BAR_WIDTH, BAR_HEIGHT)
        
        # convert weapon dictionary
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)
            
        # convert magic dictionary
        self.magic_graphics = []
        for magic in magic_data.values():
            path = magic['graphic']
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)
    
    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg first ( black rectangle )
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        
        # converting stat to pixels
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        # drawing the current value bars ( health and energy )
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, BAR_PADDING)     # give padding for bars
    
    def show_exp(self, exp):
        # converting the exp into a guaranteed integer first makes the number more consistent
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright = (WIDTH - EXP_PADDING, HEIGHT - EXP_PADDING))
        
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(EXP_PADDING, EXP_PADDING)) # background rectangle
        self.display_surface.blit(text_surf, text_rect) # rectangle text value display
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(EXP_PADDING, EXP_PADDING), BAR_PADDING) # padding to the bar
    
    def selection_box(self, left, top, has_switched):
        # background rectangle
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        
        if not has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, BAR_PADDING)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, BAR_PADDING)
        return bg_rect
        
    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(WEAPON_SELECTION_BOX_X, WEAPON_SELECTION_BOX_Y, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        
        self.display_surface.blit(weapon_surf, weapon_rect)
    
    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(MAGIC_SELECTION_BOX_X, MAGIC_SELECTION_BOX_Y, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)
        
        self.display_surface.blit(magic_surf, magic_rect)
    
    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index, player.can_switch_weapon)
        self.magic_overlay(player.magic_index, player.can_switch_magic)