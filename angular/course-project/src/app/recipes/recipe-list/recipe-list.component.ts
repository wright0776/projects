import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe.model';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipes: Recipe[] = [
    new Recipe('Test Recipe', 'Test description', 'https://veganheaven.org/wp-content/uploads/2018/01/Vegan-Bibimbap-1.jpg'),
    new Recipe('Test Recipe', 'Test description', 'https://veganheaven.org/wp-content/uploads/2018/01/Vegan-Bibimbap-1.jpg')
  ];

  constructor() { }

  ngOnInit() {
  }

}
