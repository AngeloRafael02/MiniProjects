import { Component, OnInit } from '@angular/core';
import { weaponInterface } from '../interfaces';
import { MainService } from '../main.service';

@Component({
  selector: 'app-weapon-view',
  template: ` <p>WEAPONS</p>
              <ul *ngFor="let Weapon of Weapons">
                <li>{{Weapon.name}} : {{Weapon.secondaryStat}} : {{Weapon.domain}}</li>.
              </ul>`,
  styles: [
  ]
})
export class WeaponViewComponent implements OnInit {

  public Weapons:weaponInterface[] = []

  constructor(
    private _mainService:MainService
  ) { }

  ngOnInit(): void {
    this._mainService.getWeaponView()
    .subscribe(data => this.Weapons = data);
  }

}
