import { Routes } from '@angular/router';
import { Login } from './pages/login/login';
export const routes: Routes = [
      { path: 'login', component: Login },
  // 2. (Opcional) Se acessar a raiz vazia '', redireciona direto para /login
  { path: '', redirectTo: 'login', pathMatch: 'full' }
];

