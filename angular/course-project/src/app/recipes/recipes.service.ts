import { EventEmitter, Injectable } from '@angular/core';

import { Recipe } from './recipe.model';
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';

@Injectable()
export class RecipeService {
    recipeSelected = new EventEmitter<Recipe>();

    private recipes: Recipe[] = [
        new Recipe(
            'Vegan Schnitzel',
            'A veganized version of a classic Wiener Schnitzel.',
            'https://www.elephantasticvegan.com/wp-content/uploads/2014/08/vegan-schnitzel.jpg',
            [
                new Ingredient('chicken TVP', 6, 'slices'),
                new Ingredient('chickpea flour', .33, 'cup'),
                new Ingredient('water', .33, 'cup')
            ]
        ),
        new Recipe(
            'Vegan Black Bean Burgers',
            'Easy black bean burgers for everyone!',
            'https://images.media-allrecipes.com/userphotos/560x315/5483903.jpg',
            [
                new Ingredient('black beans', 1, 'can'),
                new Ingredient('sweet onion', .33, 'cup'),
                new Ingredient('minced garlic', 1, 'tablespoon')
            ]
        )
      ];

      constructor(private shoppingListService: ShoppingListService) {}

      getRecipes() {
          return this.recipes.slice();
      }

      addRecipeIngredients(ingredients: Ingredient[]) {
        this.shoppingListService.addIngredients(ingredients);
    }
}
