import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { characterInterface,weaponInterface } from './interfaces';

@Injectable({
  providedIn: 'root'
})
export class MainService {

  constructor(
    private http:HttpClient
  ) { }

  private _characterDB_URL:string = "/assets/data/CharacterMockDB.json";
  getCharacterView():Observable<characterInterface[]>{
    return this.http.get<characterInterface[]>(this._characterDB_URL);
  }

  private _weaponDB_URL:string = "/assets/data/WeaponMockDB.json";
  getWeaponView():Observable<weaponInterface[]>{
    return this.http.get<weaponInterface[]>(this._weaponDB_URL);
  }
}
