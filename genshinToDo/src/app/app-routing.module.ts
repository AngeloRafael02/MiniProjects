import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
//COMPONENTS
import { CharacterViewComponent } from './character-view/character-view.component';
import { WeaponViewComponent } from './weapon-view/weapon-view.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { CharacterDetailsComponent } from './character-details/character-details.component';

const routes: Routes = [
  {path:'', redirectTo:'/Characters', pathMatch:'full'},
  {path:"Characters", component:CharacterViewComponent},
  {path:"Characters/:id", component:CharacterDetailsComponent},
  {path:"Weapons", component:WeaponViewComponent},
  {path:"**", component:NotFoundComponent} //Wildcard Route
];

@NgModule({
  imports: [
    CommonModule
    ,RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [
  CharacterViewComponent,
  CharacterDetailsComponent,
  WeaponViewComponent, 
  NotFoundComponent];
