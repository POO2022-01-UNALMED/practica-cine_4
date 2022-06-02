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
public class Cliente extends Persona{
    private long cedula;
    private String nombre;
    private int puntos;
     
    

    
    public Cliente(int cedula,int celular,String nombre, String sexo, int edad,int puntos)
    {   super(cedula, celular, nombre, sexo, edad);
        this.cedula = cedula;
        this.nombre = nombre;
        this.puntos = puntos;
    }
    
    public boolean confirmarCliente( Cliente confirmar )
    {
        if( cedula == confirmar.getCedula( ) )
            return true;
        else
            return false;
    }
    


    public String getNombre( )
    {
        return nombre;
    }


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}






    public boolean loging(Cliente Cliente, ArrayList<Cliente> clientes)
    {
        boolean varConfirmar = false;
        for (Cliente cli : clientes) {
            if (cli.confirmarCliente(Cliente.getCedula())) {
                varConfirmar = true;
                break;
            } 
        }
        return varConfirmar;          
    }


   

    public boolean confirmarCliente (long confirmar){
        if (confirmar == this.cedula) {
            return true;
            
        }
        return false;
    }

    public int [] localizacionCliente(ArrayList<Sala> salas, int cliente ){
        int [] localizacionCliente = new int [2];
        int i = 0;
        int varLocalizacion = -1;
        int varComparadorCliente =0;
        for (Sala sala: salas) {
            for (int j = 0; j < sala.getSillas().size(); j++) {
                varComparadorCliente = sala.getSillas().get(j).getCliente().getCedula();
                if (cliente == varComparadorCliente) {
                    varLocalizacion = j;
                    localizacionCliente[0] = varLocalizacion;
                    localizacionCliente[1] = i;

                    break;

                }
                
            }

            if (varLocalizacion != -1){
                System.out.println("El cliente esta localizado en la Sala: "+i+" y en la silla: " + i);
                break;
            }

            else{
                i++;
            }

            
        }

        return localizacionCliente;

    }

    }

   
   
    
    //si el cliente pregunta por las funciones del dia

    
    
    
    

  /*  //el cliente compra una entrada con descuento y se hace la reserva 
    public String comprarEntrada(Cliente cliente,Sala sala, int tipo, int ubicacion){
        
       
        
        if (1== tipo){ //--------> si el cliente ha elegido la opcion de vip  
             
           Sala.admin.reservar(tipo, cliente.getCedula(), cliente, sala);//----le guradamos la reserva
        
           
        }else if(2== tipo){//lo mismo pero con el cliente economico 
           
             Sala.admin.reservar(2, cliente.getCedula(), cliente, sala);
        }*/
                        
         
