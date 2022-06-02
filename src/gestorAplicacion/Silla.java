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
public class Silla {
    
    //Hacer ediciones y tocar 

    
    private int numero;
    
    private String tipo;
    
    private String ubicacion;
    
    private boolean danada=false;
    
    private Cliente clientes;

    
    public Silla( int numero, String tipo, String ubicacion, Cliente cliente )
    {
        this.numero =numero;
        this.tipo = tipo;
        this.ubicacion = ubicacion;
        this.clientes = cliente;
    }

    
    public void asignarAcliente( Cliente cliente)
    {
        this.clientes = cliente;
    }

    
    public void desasignarSilla( )
    {
        clientes = null;
    }

    
    public boolean sillaAsignada( )
    {
        if( null == clientes )
            return false;
        else
            return true;
    }

    
    public boolean sillaAsignadaAcliente( Cliente p )
    {
        if( null == clientes )
            return false;
        else if( clientes.confirmarCliente(p ) )
            return true;
        else
            return false;
    }

    
    public int getNumero( )
    {
        return numero;
    }

    
    public String getTipo( )
    {
        return tipo;
    }

    
    public String getUbicacion( )
    {
        return ubicacion;
    }

    
    public Cliente getCliente( )
    {
        return clientes;
    }

    public boolean isDanada() {
        return danada;
    }

    public void setDanada(boolean danada) {
        this.danada = danada;
    }
    
    
}