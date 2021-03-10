package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/*
 * 숙제 : MyFrame02 만들고, Jlabel 넣고 (lbl) 숫자넣고 버튼 Jbtn(btn) 만들고, 클릭하면 라벨에 써있는 숫자가 계속 증가하게끔 구현하기. 
 */

public class MyFrame02 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame02 frame = new MyFrame02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("0");
		lbl.setBounds(36, 38, 117, 80);
		contentPane.add(lbl);
		
		JButton btn = new JButton("click to increase");
		btn.setBounds(185, 35, 125, 89);
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int number = Integer.parseInt(lbl.getText());
				lbl.setText(String.valueOf(number+1));
			}
		});
		contentPane.add(btn);
	}

}
