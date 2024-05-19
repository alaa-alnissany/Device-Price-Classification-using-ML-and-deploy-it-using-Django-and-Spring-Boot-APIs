package com.DevicePriceClassifier.Api.Model;


public class Devices {
    public int battery_power;
    public boolean blue;
    public double clock_speed;
    public boolean dual_sim;
    public int fc;
    public boolean four_g;
    public int int_memory;
    public double m_dep;
    public int mobile_wt;
    public int n_cores;
    public int pc;
    public int px_height;
    public int px_width;
    public int ram;
    public int sc_h;
    public int sc_w;
    public int talk_time;
    public boolean tree_g;
    public boolean touch_screen;
    public boolean wifi;
    private boolean intToBool(int value) {
        return value != 0;
    }
    public void put(String param, Object value) {
        switch (param) {
            case "battery_power":
                this.battery_power = (int) value;
                break;
            case "blue":
                this.blue = intToBool((int)value);
                break;
            case "clock_speed":
                this.clock_speed = (double) value;
                break;
            case "dual_sim":
                this.dual_sim = ((int) value) != 0;
                break;
            case "fc":
                this.fc = (int) value;
                break;
            case "four_g":
                this.four_g = ((int) value) != 0;
                break;
            case "int_memory":
                this.int_memory = (int) value;
                break;
            case "m_dep":
                this.m_dep = (double) value;
                break;
            case "mobile_wt":
                this.mobile_wt = (int) value;
                break;
            case "n_cores":
                this.n_cores = (int) value;
                break;
            case "pc":
                this.pc = (int) value;
                break;
            case "px_height":
                this.px_height = (int) value;
                break;
            case "px_width":
                this.px_width = (int) value;
                break;
            case "ram":
                this.ram = (int) value;
                break;
            case "sc_h":
                this.sc_h = (int) value;
                break;
            case "sc_w":
                this.sc_w = (int) value;
                break;
            case "talk_time":
                this.talk_time = (int) value;
                break;
            case "tree_g":
                this.tree_g = ((int) value) != 0;
                break;
            case "touch_screen":
                this.touch_screen = ((int) value) != 0;
                break;
            case "wifi":
                this.wifi = ((int) value) != 0;
                break;
            default:
                throw new IllegalArgumentException("Invalid parameter: " + param);
        }
    }
}