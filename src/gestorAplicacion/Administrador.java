/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


package gestorAplicacion;

import java.util.ArrayList;

/**
 *
 * @author usuario
 */

/*
public class Administrador extends Trabajador {
    
    private int Salario;
    private int cedula;
    private String nombre;
    private int edad;

    
    
    
    
    public Administrador(String nombre, int id, int edad){
        super( nombre,  id,  "Administrador",  edad, true);
        this.nombre=nombre;
        this.edad=edad;
        this.Salario=1500000;
        
                
    }
    
    
    public String EliminarPelicula(Pelicula pelicula){
       String a="";
       ArrayList<String> pelis= new ArrayList<>();
        for(int i=0; i< Pelicula.peliculas.size();i++){
            Pelicula p = Pelicula.peliculas.get(i);
            if(pelicula==p){
                pelis.remove(pelicula);
                a= "Se elimino con exito";
            }else{
                a="No se encontro la pelicula";
            }
      }
        return a;
   }
    
   
    public String agregarPelicula(Pelicula pelicula){
        
    String a="";
       ArrayList<String> pelis= new ArrayList<>();
        for(int i=0; i< Pelicula.peliculas.size();i++){
            Pelicula p = Pelicula.peliculas.get(i);
            if(pelicula!=p){
                Pelicula.peliculas.add(pelicula);
                a= "Se agrego con exito";
            }else{
                a="la pelicula pelicula ya esta";
            }
      }
        return a;
   }
    
   
     
    //aqui hacemos la rserva del cliente 
    public void reservar(int tipo, int ubicacion, Cliente cliente, Sala reserva){
        
        String tip="";
        String tip2="";
        
        Silla silla=null;
        
        if (tipo==silla.SILLAS_ECONOMICAS){    //aqui asignamos que si la silla va ser vip o economica
            
            
            tip="Silla_Economica";
            
            silla=reserva.asignarSilla(2, ubicacion, cliente);
        }
        else if (tipo==silla.SILLAS_VIP){
            silla=reserva.asignarSilla(1, 2, cliente);
            tip="Silla_Vip";
        }
        
        
       
                
        if (ubicacion==1) {
            
                tip2="Lateral_Derecho";
                
                
        } else if(ubicacion==2){
                tip2="Central";
                
    }else{
                tip2="Lateral_Izquierdo";
                
        }
        System.out.println( "Numero: " + silla.getNumero()
                +"\nTipo: " + tip
                + "\nUbicacion: "+ tip2);
     }
    
    
    public String estadisticas(Sala sala){
        return ("Numero de sillas dañadas: " + sala.contarSillasDanadas()
                  +"\nSillas economicas ocupadas: "+sala.contarSillasEconomicasOcupadas()
                 +"\nSillas vip ocupadas: "+ sala.contarSillasVipOcupadas()
                +"\nSillas vip libres: "+sala.obtenerSillasVip()
                +"\nSillas Economicas libres: " +sala.darSillasVacias());
    }
    
    
    
    
    
    
    
}*/
