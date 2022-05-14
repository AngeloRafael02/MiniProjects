import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { weaponInterface } from '../interfaces';
import { MainService } from '../main.service';

@Component({
  selector: 'app-weapon-view',
  template: ` <p>WEAPONS</p>
              <ul *ngFor="let Weapon of Weapons">
                <li (click)="onSelect(Weapon)" [class.selected]="wasSelected(Weapon)">{{Weapon.name}}</li>
              </ul>`,
  styles: [`
  li.selected{
    color:red;
  }  `]
})
export class WeaponViewComponent implements OnInit {

  public Weapons:weaponInterface[] = []
  public weaponNumber:number = 0;

  constructor(
    private _mainService:MainService,
    private route:ActivatedRoute,
    private router:Router
  ) { }

  ngOnInit(): void {
    this._mainService.getWeaponView()
    .subscribe(data => this.Weapons = data);

    this.route.paramMap.subscribe((params:any)=>{
      let id = parseInt(params.get('id'));
      this.weaponNumber = id;
    })
  }

  onSelect(Weapon:weaponInterface):void{
    this.router.navigate(['/Weapons',Weapon.id])
  }

  wasSelected(Weapon:any):boolean{
    return Weapon.id === this.weaponNumber
  }

}
