import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
//COMPONENTS
import { CharacterViewComponent } from './character-view/character-view.component';
import { WeaponViewComponent } from './weapon-view/weapon-view.component';

const routes: Routes = [
  {path:"Characters", component:CharacterViewComponent},
  {path:"Weapons", component:WeaponViewComponent},
];

@NgModule({
  imports: [
    CommonModule
    ,RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [CharacterViewComponent, WeaponViewComponent];
